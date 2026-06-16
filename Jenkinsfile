pipeline{
    agent any
        stages{
            stage ('stage one get code'){
                steps{
                    git branch : 'main',
                    url : 'https://github.com/prachimagadum06-ops/pythonfrompipelineproject.git'
                }
            }
            stage ('stage two check python'){
                steps{
                    bat '"C:\\Users\\Dell\\AppData\\Local\\Python\\bin\\python.exe" --version'
                }
            }
            stage ('stage three install pip'){
                steps{
                    bat """
                    pip install -r requirements.txt
                    """
                }
            }
            stage ('stage four run app'){
                steps{
                
                bat '"C:\\Users\\Dell\\AppData\\Local\\Python\\bin\\python.exe" app.py'
                    
                }
            }
        }

    
}