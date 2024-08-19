from pydantic import BaseModel, EmailStr, ValidationError
import pandas as pd

# Define a Pydantic model with email validation
class UserModel(BaseModel):
    email: EmailStr

# Sample DataFrame with an 'email' column
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Email': ['alice@example.com', 'bob.example@com', 'charlie@domain', 'david@domain.com']
}

df = pd.DataFrame(data)

# Function to validate email using Pydantic
def validate_email(email):
    try:
        # Validate the email using the UserModel
        UserModel(email=email)
        return True
    except ValidationError:
        return False

# Apply the validation function to the DataFrame
df['is_valid_email'] = df['Email'].apply(validate_email)

# Display the DataFrame with validation results
print(df)
