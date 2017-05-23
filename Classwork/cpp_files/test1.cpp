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
	
	
	xxxxx temp_addres = 
	{
		0,  // street_no
		"",  // street_name
		"Hamilton",  // city
		"Ontario",  // prov
		"",  // postal_code
	};
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
	for (i=0;i<3;i++)
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
	
	
	cout << temp_addres.street_no << endl << temp_addres.street_name << endl << temp_addres.city << endl << temp_addres.prov << endl << temp_addres.postal_code << endl;
	temp_addres.street_no = 26;
	cout << "Մուտքագրեք փողոցի անունը։ ";
	cin>>temp_addres.street_name;
	temp_addres.postal_code = "2001";
	cout << endl;
	cout << temp_addres.street_no << endl << temp_addres.street_name << endl << temp_addres.city << endl << temp_addres.prov << endl << temp_addres.postal_code << endl;
	//cout << endl;
	//cout << &temp_addres.street_no << endl << &temp_addres.street_name << endl << &temp_addres.city << endl << &temp_addres.prov << endl << &temp_addres.postal_code << endl;
	return 0;
}
