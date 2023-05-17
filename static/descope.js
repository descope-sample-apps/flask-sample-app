const projectId = "P2Pq03wpnnjxJajSUKDuy2xviLNV"
const sdk = Descope({ projectId: projectId, persistTokens: true, autoRefresh: true });
const sessionToken = sdk.getSessionToken()
var notValidToken

if (sessionToken) {
    notValidToken = sdk.isJwtExpired(sessionToken)
}