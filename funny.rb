require 'openssl'
require 'jwt'  # https://rubygems.org/gems/jwt

# Private key contents
private_pem = File.read("/home/cappy/Downloads/builds-per-minute.2022-06-01.private-key.pem")
private_key = OpenSSL::PKey::RSA.new(private_pem)

# Generate the JWT
payload = {
  # issued at time, 60 seconds in the past to allow for clock drift
  iat: Time.now.to_i - 60,
  # JWT expiration time (10 minute maximum)
  exp: Time.now.to_i + (10 * 60),
  # GitHub App's identifier
  iss: "206650"
}

jwt = JWT.encode(payload, private_key, "RS256")
puts jwt

# export envar "jwt" to use in curl
#exec "export jwt='#{jwt}'"
exec "curl -X POST -H \"Accept: application/vnd.github.v3+json\" https://api.github.com/app/installations/26150114/access_tokens -H \"Authorization: Bearer #{jwt}\""