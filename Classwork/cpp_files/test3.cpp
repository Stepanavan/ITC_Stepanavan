#include <iostream>
#include <string>
using namespace std;
int main()
{
	struct xxxxx
	{
		int street_no;
		string street_name;
		string city;
		string prov;
		string postal_code;
	};
	
	struct mard
	{
	
		string name;
		string surname;
		short age;
		short hasak;
		string azgutyun;
		xxxxx address;
	};
	
	/*mard temp_mard; 
	cin >>temp_mard.name;
	cin >>temp_mard.surname;
	cin >>temp_mard.age;
	cin >>temp_mard.hasak;
	cin >>temp_mard.azgutyun;
	cin >>temp_mard.address.street_no;
	cin >>temp_mard.address.street_name;
	cin >>temp_mard.address.city;
	cin >>temp_mard.address.prov;
	cin >>temp_mard.address.postal_code;
		
	cout<<temp_mard.name;
	cout<<temp_mard.surname;
	cout<<temp_mard.age;
	cout<<temp_mard.hasak;
	cout<<temp_mard.azgutyun;
	cout<<temp_mard.address.street_no;
	cout<<temp_mard.address.street_name;
	cout<<temp_mard.address.city;
	cout<<temp_mard.address.prov;
	cout<<temp_mard.address.postal_code;
	*/
		
	xxxxx hascener[3];
	int i;
	for (i=0;i<3;i++)
	{
		cout << "Մուտքագրեք շենքի համարը ";
		cin >> hascener[i].street_no;
		cout << "Մուտքագրեք փողոցի անունը։ ";
		cin >> hascener[i].street_name;
		cout << "Մուտքագրեք քաղաքը։ ";
		cin >> hascener[i].city;
		cout << "Մուտքագրեք մարզը։ ";
		cin >> hascener[i].prov;
		cout << "Մուտքագրեք փոստային ինդեքսը։ ";
		cin >> hascener[i].postal_code;
	}
	cout << "inch pntrel"  <<endl;
	int a;
	cin >> a;
	for (i=0;i<3;i++)
	{
		if (hascener[i].street_no==a)
		{
			cout << "շենքի համարը ";
			cout << hascener[i].street_no << endl; 
			cout << "փողոցի անունը։ ";
			cout << hascener[i].street_name << endl;;
			cout << "քաղաքը։ ";
			cout << hascener[i].city << endl;
			cout << "մարզը։ ";
			cout << hascener[i].prov << endl;
			cout << "փոստային ինդեքսը։ ";
			cout << hascener[i].postal_code << endl;
		}
	
	}
	
	
	return 0;
}
