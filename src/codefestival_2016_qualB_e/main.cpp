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


ll gcd(ll a, ll b) { return b ? gcd(b, a % b) : a; }

auto solve(int a, const std::vector<std::string> &b, int c, const std::vector<ll> &d, const std::vector<std::string> &e) {
  // TODO: edit here
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int a, c;
  std::cin >> a;
  std::vector<std::string> b(a);
  rep (i, a) {
    std::cin >> b[i];
  }
  std::cin >> c;
  std::vector<ll> d(c);
  std::vector<std::string> e(c);
  rep (i, c) {
    std::cin >> d[i] >> e[i];
  }

  auto ans = solve(a, b, c, d, e);
  rep (i, c) {
    std::cout << f[i] << '\n';
  }

  return 0;
}
