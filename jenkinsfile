pipeline{
    agent any
        stages{
            stage 'stage one get code'{
                steps{
                    git branch : 'main',
                    url : 'https://github.com/prachimagadum06-ops/pythonfrompipelineproject.git'
                }
            }
            stage 'stage two check python'{
                steps{
                    bat  """python --version"""
                }
            }
            stage 'stage three install pip'{
                steps{
                    bat """
                    pip install -r requirements.txt
                    """
                }
            }
            stage 'stage four run app'{
                steps{
                    bat """
                    python app.py
                    """
                }
            }
        }

    
}