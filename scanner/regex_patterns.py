TOKEN_PATTERNS = [
    r"(?i)(AKIA[0-9A-Z]{16})",  # AWS Access Key
    r"(?i)AIza[0-9A-Za-z\-_]{35}",  # Google API Key
    r"(?i)ghp_[A-Za-z0-9]{36}",  # GitHub Personal Access Token
    r"(?i)[0-9a-f]{32}",  # Generic MD5-like hashes
    r"(?i)[A-Za-z0-9\-_]{32}",  # Generic API keys
    r"(?i)sk_live_[0-9a-zA-Z]{24}",  # Stripe Secret Key
    r"(?i)Bearer\s([A-Za-z0-9\-_]{32,})",  # OAuth Bearer Token
    r"(?i)sf_[A-Za-z0-9]{17}",  # Salesforce Token
    r"(?i)v1\.[0-9a-zA-Z]{22}",  # Twilio Auth Token
    r"(?i)S[-_0-9A-Za-z]{36}",  # Slack API Token
    r"(?i)[0-9a-fA-F]{64}",  # SHA-256 Hashes
    r"(?i)P([0-9A-F]{8})[-_][0-9A-F]{8}",  # PayPal Access Token
]

