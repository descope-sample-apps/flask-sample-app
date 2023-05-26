const projectId = "P2QISti0x5gz0jXkMWwLKY3VZDcJ"
const sdk = Descope({ projectId: projectId, persistTokens: true, autoRefresh: true })

const sessionToken = sdk.getSessionToken()

// const refreshToken = sdk.getRefreshToken()
// const validRefreshToken = refreshToken && !sdk.isJwtExpired(refreshToken)