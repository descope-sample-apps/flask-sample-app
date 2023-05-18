const projectId = "P2PvuraQbUIEivQPBGbxO9M7O8Qy"
const sdk = Descope({ projectId: projectId, persistTokens: true, autoRefresh: true });
const sessionToken = sdk.getSessionToken()
var notValidToken

if (sessionToken) {
    notValidToken = sdk.isJwtExpired(sessionToken)
}