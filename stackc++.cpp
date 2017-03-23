#include <iostream>
#include <vector>

using namespace std;
template <class T>
class Stack{
	private:
		vector<T> liste;
	public:
		void push(T elem){
			liste.push_back(elem);
		}
		T pop(){
			return liste.pop_back();
		}
		T top(){
			return liste.back();
		}
		int size(){
			return liste.length();
		}
};


int main(){
	Stack<int> intStack;
	intStack.push(7);
	cout<<intStack.top()<<endl;
	return 0;
}
