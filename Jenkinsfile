def projectName = 'RestApiProject'
def version = "0.0.${currentBuild.number}"
def dockerImageTag = "${projectName}:${version}"

pipeline {
  agent any

  stages {
    stage('Test') {
      steps {
        sh 'pip install -r requirements.txt && python main.py'
        

      }
    }

    stage('Build') {
      steps {
       sh 'echo "building the repo"'
      }
    }

    stage('Build Container') {
      steps {
        sh "docker build -t ${dockerImageTag} ."
      }
    }

    stage('Deploy Container To Openshift') {
      steps {
        sh "oc login https://localhost:8443 --username admin --password admin --insecure-skip-tls-verify=true"
        sh "oc project ${projectName} || oc new-project ${projectName}"
        sh "oc delete all --selector app=${projectName} || echo 'Unable to delete all previous openshift resources'"
        sh "oc new-app ${dockerImageTag} -l version=${version}"
        sh "oc expose svc/${projectName}"
      }
    }
  }
}
