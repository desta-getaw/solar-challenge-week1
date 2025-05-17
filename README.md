# Solar Challenge Week 1

## Environment Setup

Follow these steps to reproduce the development environment:

### Prerequisites
- Python 3.9+ (recommended 3.11)
- Git
- pip (Python package manager)

### 1. Clone the repository
```bash
git clone https://github.com/your-username/solar-challenge-week1.git
cd solar-challenge-week1
###2. Create and activate a virtual environment
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install dependencies

pip install -r requirements.txt
4. Verify the installation

python --version
pip list
5. Running the project
# Example command to run main script
python src/main.py
### Development Workflow
#Create a new branch for your work:
git checkout -b your-feature-branch
#After making changes, run tests (if available):
python -m pytest
#Commit your changes:
git add .
git commit -m "description of changes"
git push origin your-feature-branch
