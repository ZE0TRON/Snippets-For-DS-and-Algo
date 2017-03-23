#include <iostream>
#include <vector>

using namespace std;
template <class T>
class Queue{
	private:
		vector<T> liste;
	public:
		void enqueue(T elem){
			liste.push_back(elem);
		}
		T dequeue(){
			T a = liste[0]; //İlk eleman
			liste.erase(liste.begin()); // En başın indexini sil
			return a; // İlk elemanı Returnle
		}
		T top(){
			return liste[0];
		}
	};
int main(){
	Queue<int> intQueue;
	intQueue.enqueue(7); //7 yi ekle
	intQueue.enqueue(11); //11'i ekle
	cout<<intQueue.top()<<endl; // İlk değeri yazdır
	intQueue.dequeue(); // İlk değeri sil
	cout<<intQueue.dequeue()<<endl; //İlk değeri silerken çıkartılan değeri bastır
	return 0;
}
