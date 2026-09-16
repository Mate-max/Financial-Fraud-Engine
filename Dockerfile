# 1. Python-ის ოფიციალური მსუბუქი იმიჯი
FROM python:3.10-slim

# 2. სამუშაო დირექტორიის განსაზღვრა კონტეინერში
WORKDIR /app

# 3. დამოკიდებულებების კოპირება და ინსტალაცია
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. პროექტის კოდისა და ნასწავლი მოდელის კოპირება
COPY app/ ./app/
COPY src/ ./src/
COPY models/ ./models/

# 5. FastAPI-ის პორტის გახსნა
EXPOSE 8000

# 6. სერვერის გაშვება
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]