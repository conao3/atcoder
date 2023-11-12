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

ll solve(int W, int H, const std::vector<ll> &p, const std::vector<ll> &q) {
  // TODO: edit here
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int W, H;
  std::cin >> W;
  std::vector<ll> p(W);
  std::cin >> H;
  std::vector<ll> q(H);
  rep (i, W) {
    std::cin >> p[i];
  }
  rep (i, H) {
    std::cin >> q[i];
  }

  auto ans = solve(W, H, p, q);
  std::cout << ans << '\n';

  return 0;
}
