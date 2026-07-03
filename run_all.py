import subprocess
import sys

tests = [
    "tests.test_login",
    "tests.test_google_login",
    "tests.test_signup",
    "tests.test_forgot_password",
    "tests.test_login_empty",
    "tests.test_login_invalid_email",
    "tests.test_login_invalid_pass"
]

for test in tests:
    print(f"\n{'='*15} Running {test} {'='*15}\n")
    subprocess.run([sys.executable, "-m", test])