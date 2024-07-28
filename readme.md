# generate password for kubernetes secret

echo -n "<password-value>" | base64

uvicorn main:app --reload