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

auto solve(int k, int q, const std::vector<ll> &d, const std::vector<ll> &n, const std::vector<ll> &x, const std::vector<ll> &m) {
  // TODO: edit here
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int k, q;
  std::cin >> k;
  std::vector<ll> d(k);
  std::cin >> q;
  std::vector<ll> n(q), x(q), m(q);
  rep (i, k) {
    std::cin >> d[i];
  }
  rep (i, q) {
    std::cin >> n[i] >> x[i] >> m[i];
  }

  auto ans = solve(k, q, d, n, x, m);
  rep (i, q) {
    std::cout << a[i] << '\n';
  }

  return 0;
}
