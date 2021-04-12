#include <iostream>
#include <unordered_map>
using namespace std;

string b16_decode(string enc, unordered_map<char, int>* mp);
char shift(char c, char k);
string get_key(long long seed);
bool check(string* flag);

int main(int argc, char *argv[]){
        string encrypted = "eljodmjdjcnfcdmgbleojbgngojkkdpimebgeigpdkjpmgngpfpgelemjoglghjd";
        string ALPHABET = "abcdefghijklmnop";

        unordered_map<char, int> mp;
        for(int i=0; i<(int)ALPHABET.size(); i++) {
                mp[ALPHABET[i]]=i;
        }
        long long seed_min = stoll(argv[1]);
        long long seed_max = stoll(argv[2]);


        for(long long seed=seed_min; seed<seed_max; seed++) {
                string key = get_key(seed);
                string dec="";
                for(long long i=0; i<(long long)encrypted.size(); i++) {
                        char c = encrypted[i];
                        dec+=shift(c,key[i%key.size()]);
                }
                string flag = b16_decode(dec, &mp);
                if(check(&flag)) {
                        cout<<"key:"<<key<<" flag:"<<flag<<endl;
                }
        }
}

char shift(char c, char k){
        string ALPHABET = "abcdefghijklmnop";
        return ALPHABET[(c-'a'+k-'a')%ALPHABET.size()];
}

string b16_decode(string enc, unordered_map<char, int>* mp){
        string plain="";
        for(long long i=0; i<(long long)enc.size(); i+=2) {
                int ind1 = (*mp)[enc[i]];
                int ind2 = (*mp)[enc[i+1]];
                plain+=(char)(ind1*16+ind2);
        }
        return plain;
}


string get_key(long long seed){
        string ALPHABET = "abcdefghijklmnop";
        string key="";
        while(seed>0) {
                key+=ALPHABET[seed%ALPHABET.size()];
                seed=seed/ALPHABET.size();
        }
        return key;
}

bool check(string* _flag){
        string flag = *_flag;
        for(long long i=0; i<(long long)flag.size(); i++) {
                if(!(('a'<=flag[i] and flag[i]<='f') or ('0'<=flag[i] and flag[i]<='9'))) {
                        return false;
                }
        }
        return true;
}
