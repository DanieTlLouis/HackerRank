/*
Lexicographical* order is often known as alphabetical order when dealing with
strings. A string is greater than another string if it comes later in a
lexicographically sorted list.
Given a word, create a new word by swapping some or all of its characters. This
new word must meet two criteria:
    It must be greater than the original word
    It must be the smallest word that meets the first condition
* https://en.wikipedia.org/wiki/Lexicographical_order *
Example
    w=abcd
    The next largest word is abdc.
    Complete the function biggerIsGreater below to create and return the new
    string meeting the criteria. If it is not possible, return no answer.
Function Description
    Complete the biggerIsGreater function in the editor below.
    biggerIsGreater has the following parameter(s):
        string w: a word
Returns
    - string: the smallest lexicographically higher string possible or no answer
Input Format
    The first line of input contains T, the number of test cases.
    Each of the next T lines contains w.
Constraints
    1<=T<=10^5
    1<=lengthofw<=100
    w will contain only letters in the range ascii[a..z].
Sample Input 0
    5
    ab
    bb
    hefg
    dhck
    dkhc
Sample Output 0
    ba
    no answer
    hegf
    dhkc
    hcdk
Explanation 0
    Test case 1:
        ba is the only string which can be made by rearranging ab. It is
        greater.
    Test case 2:
        It is not possible to rearrange bb and get a greater string.
    Test case 3:
        hegf is the next string greater than hefg.
    Test case 4:
        dhkc is the next string greater than dhck.
    Test case 5:
        hcdk is the next string greater than dkhc.
Sample Input 1
    6
    lmno
    dcba
    dcbb
    abdc
    abcd
    fedcbabcd
Sample Output 1
    lmon
    no answer
    no answer
    acbd
    abdc
    fedcbabdc
*/

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'biggerIsGreater' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING w as parameter.
 */

string biggerIsGreater(string w) {
    int target = -1;
    int target2 = -1;
    for(int i=w.size()-1;i>=0;i--){
        if(w[i]-'a'>w[i-1]-'a'){
            target = i-1;
            break;
        }
    }
    if(target==-1){
        return "no answer";
    }
    for(int i=w.size()-1;i>=0;i--){
        if(w[i]-'a'>w[target]-'a'){
            target2=i;
            break;
        }
    }
    swap(w[target],w[target2]);
    reverse(w.begin()+target+1,w.end());
    return w;
    /*
    string s = w.substr(0,w.length()-2);
    s = s + w[w.length()-1] + w[w.length()-2];
    if(s <= w)
    {
        return "no answer";
    }
    return s;
    */
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string T_temp;
    getline(cin, T_temp);

    int T = stoi(ltrim(rtrim(T_temp)));

    for (int T_itr = 0; T_itr < T; T_itr++) {
        string w;
        getline(cin, w);

        string result = biggerIsGreater(w);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
