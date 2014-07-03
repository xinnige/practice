public class MultiThreadExample{
	public static String stuff = " printing material";

	public static void main(String[] args){
		Thread t1 = new Thread(new RunnableProcess());
		Thread t2 = new Thread(new RunnableProcess());

		t1.setName("T-1");
		t2.setName("T-2");

		t2.start();
		t1.start();
	}

	public static void printFor(int index){
		StringBuffer sb = new StringBuffer();
		sb.append(Thread.currentThread().getName()).append(stuff);
		sb.append(" for the ").append(index).append(" time.");
		System.out.println(sb.toString());
	}

}

class RunnableProcess implements Runnable{
	public void run(){
		for (int i = 0; i < 10; i++){
			//MultiThreadExample.printFor(i);
			synchronized(MultiThreadExample.stuff){
				MultiThreadExample.printFor(i);
				try{
					MultiThreadExample.stuff.notifyAll();
					MultiThreadExample.stuff.wait();
					MultiThreadExample.stuff.notifyAll();
				} catch (InterruptedException ex){
					ex.printStackTrace();
				}
			}

		}
	}	
}
