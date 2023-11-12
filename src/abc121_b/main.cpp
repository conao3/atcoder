#include <iostream>
#include <vector>

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

ll solve(ll n, ll m, ll c, const vector<ll> &b, const vector<vector<ll>> &a) {
  ll ans = 0;
  for (auto &elm: a) {
    ll sum = 0;
    for (int i = 0; i < m; ++i) {
      sum += elm[i] * b[i];
    }
    if (sum + c > 0) {
      ++ans;
    }
  }
  return ans;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  ll n, m, c;
  cin >> n >> m >> c;
  vector<ll> b(m);
  vector<vector<ll>> a(n, vector<ll>(m));
  rep (i, m) {
    cin >> b[i];
  }
  rep (i, n) {
    rep (j, m) {
      cin >> a[i][j];
    }
  }

  auto ans = solve(n, m, c, b, a);
  cout << ans << '\n';

  return 0;
}
