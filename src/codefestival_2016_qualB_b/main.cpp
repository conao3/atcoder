#include <iostream>

using namespace std;

typedef long long   ll;
typedef long double ld;

#define rep(i, n)      for (int i = 0; i < (int)(n); ++i)
#define rep3(i, m, n)  for (int i = (m); i < (int)(n); ++i)
#define rrep(i, n)     for (int i = (int)(n)-1; i >= 0; --i)
#define rrep3(i, m, n) for (int i = (int)(n)-1; i >= (m); --i)

#define endl '\n'
#define INF  0x7f7f7f7f7f7f7f7f
#define INFi 0x7f7f7f7f
const std::string YES = "Yes";
const std::string NO = "No";

ll gcd(ll a, ll b) { return b ? gcd(b, a % b) : a; }

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  ll N, A, B;
  std::string S;
  std::cin >> N >> A >> B >> S;

  ll passed = 0;
  ll passed_overseas = 0;
  for (auto s: S) {
    if (s == 'a') {
      if (passed < A + B) {
        std::cout << YES << '\n';
        ++passed;
      } else {
        std::cout << NO << '\n';
      }
    } else if (s == 'b') {
      if (passed < A + B && passed_overseas < B) {
        std::cout << YES << '\n';
        ++passed;
        ++passed_overseas;
      } else {
        std::cout << NO << '\n';
      }
    } else {
      std::cout << NO << '\n';
    }
  }

  return 0;
}
