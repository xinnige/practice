openssl genrsa -out ca.key 2048
openssl req -new -x509 -days 365 -key ca.key -subj "/C=CN/ST=ZJ/L=HZ/O=local.example.com/CN=local.example.com" -out ca.crt

openssl req -newkey rsa:2048 -nodes -keyout server.key -subj "/C=CN/ST=ZJ/L=HZ/O=local.example.com/CN=local.example.com" -out server.csr
openssl x509 -req -extfile <(printf "subjectAltName=DNS:example.com,DNS:local.example.com,DNS:www.example.com") -days 365 -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt


etcd --name infra0 --data-dir infra0 \
  --cert-file=$PWD/cert/server.crt --key-file=$PWD/cert/server.key \
  --advertise-client-urls=https://127.0.0.1:2379 --listen-client-urls=https://127.0.0.1:2379


ETCDCTL_API=3 etcdctl --cacert="$PWD/ca.crt" --key="$PWD/server.key"  --cert="$PWD/server.crt"  --endpoints=https://local.example.com:2379 put ${PATH} ${CONTENT}

etcdctl  --endpoints=https://local.example.com:2379  role add root
Role root created

etcdctl  --endpoints=https://local.example.com:2379  user add root
Password of root: 
Type password of root again for confirmation: 
User root created

etcdctl  --endpoints=https://local.example.com:2379   user  grant-role  root root
Role root is granted to user root

etcdctl  --endpoints=https://local.example.com:2379  auth enable                 
Authentication Enabled


docker run -d -p 2379:2379 -p 2380:2380 --name ${NAME} quay.io/coreos/etcd:latest /usr/local/bin/etcd --data-dir=/etcd-data --name node1 --initial-advertise-peer-urls http://0.0.0.0:2380 --listen-peer-urls http://0.0.0.0:2380 --advertise-client-urls http://0.0.0.0:2379 --listen-client-urls http://0.0.0.0:2379   --initial-cluster node1=http://0.0.0.0:2380