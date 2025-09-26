
# Test Cases – Login (Sample)

## TC-LOGIN-001 – Valid login
- Steps: Open /login → enter valid email/pass → Submit
- Expected: Redirect to /dashboard; session cookie set; 200 responses for bootstrap APIs

## TC-LOGIN-002 – Invalid password
- Steps: Enter valid email + wrong password
- Expected: Error message; no session; 401 on auth API; rate-limit counter increments

## TC-LOGIN-003 – Locked account
- Steps: Use locked user
- Expected: Error banner with support link; audit event created

## TC-LOGIN-004 – Security
- Steps: Attempt XSS in email field
- Expected: Input sanitized; no script execution; 400/422 server-side validation
