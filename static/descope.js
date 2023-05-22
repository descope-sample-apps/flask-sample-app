const projectId = "P2Pq03wpnnjxJajSUKDuy2xviLNV"
const sdk = Descope({ projectId: projectId, persistTokens: true, autoRefresh: true })

const sessionToken = sdk.getSessionToken()

const refreshToken = sdk.getRefreshToken()
const validRefreshToken = refreshToken && !sdk.isJwtExpired(refreshToken)
if (validRefreshToken) {
    sdk.refresh()
}