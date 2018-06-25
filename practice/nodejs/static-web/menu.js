angular
  .module('demoBasic', ['ngMaterial'])
  .controller('BasicDemoCtrl', function DemoCtrl($scope) {
    this.resource_types = JSON.parse('{"OS__Cinder__Volume":{"class":"fa-hdd-o","name":"OS::Cinder::Volume","code":"","color":"#0bb238"},"OS__Cinder__VolumeAttachment":{"class":"fa-plug","name":"OS::Cinder::VolumeAttachment","code":"","color":"#0bb238"},"OS__Heat__ResourceGroup":{"class":"fa-server","name":"OS::Heat::ResourceGroup","code":"","color":"#0bb238"},"OS__Neutron__FloatingIP":{"class":"fa-neuter","name":"OS::Neutron::FloatingIP","code":"","color":"#40a5f2"},"OS__Neutron__FloatingIPAssociation":{"class":"fa-paperclip","name":"OS::Neutron::FloatingIPAssociation","code":"","color":"#40a5f2"},"OS__Neutron__Net":{"class":"fa-cloud","name":"OS::Neutron::Net","code":"","color":"#40a5f2"},"OS__Neutron__Port":{"class":"fa-genderless","name":"OS::Neutron::Port","code":"","color":"#40a5f2"},"OS__Neutron__Router":{"class":"fa-life-bouy","name":"OS::Neutron::Router","code":"","color":"#40a5f2"},"OS__Neutron__RouterInterface":{"class":"fa-sun-o","name":"OS::Neutron::RouterInterface","code":"","color":"#40a5f2"},"OS__Neutron__SecurityGroup":{"class":"fa-shield ","name":"OS::Neutron::SecurityGroup","code":"","color":"#40a5f2"},"OS__Neutron__Subnet":{"class":"fa-cloud-upload ","name":"OS::Neutron::Subnet","code":"","color":"#40a5f2"},"OS__Nova__KeyPair":{"class":"fa-key ","name":"OS::Nova::KeyPair","code":"","color":"#483dff"},"OS__Nova__Server":{"class":"fa-desktop ","name":"OS::Nova::Server","code":"","color":"#483dff"},"OS__Swift__Container":{"class":"fa-archive ","name":"OS::Swift::Container","code":"","color":"#0bb238"}}');
    this.project_types = {};
    for (var idx in this.resource_types){
      var pidx = idx.split('__');
      if (!pidx || pidx.length != 3){
        continue
      }
      level1 = pidx[0]+'::'+pidx[1]
      if (! (level1 in this.project_types)){
        this.project_types[level1] = {}
      }
      this.project_types[level1][pidx[2]] = this.resource_types[idx];
    }
    $scope.currentNavItem = Object.keys(this.project_types)[0];

  });