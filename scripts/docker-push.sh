#!/usr/bin/env bash
function login_ecs(){
    echo "Logging to Gitlab"
    docker login -u $GITLAB_USERNAME -p $GITLAB_PERSONAL_ACCESS_TOKEN $GITLAB_REGISTRY

    if [ $? -eq 0 ]
    then
        echo "Successfully logged into Gitlab"
    else
        echo "Login failed"
        exit 1
    fi
}

function get_branch_name(){
    echo "Getting branch name..."

    BRANCH_NAME="$(git branch | grep \* | cut -d ' ' -f2)"
    if [ $? -eq 0 ]; then
        echo "branch_name: ${BRANCH_NAME}"
    else
        echo "branch_name could not be fetched"
        exit 1
    fi

}

function get_commit_id(){
    echo "Getting commit id..."
    COMMIT_ID="$(git log --format="%H" -n 1)"
    if [ $? -eq 0 ]; then
        echo "commit_id: ${COMMIT_ID}"
    else
        echo "commit_id could not be fetched"
        exit 1
    fi
}

function predictor_build_and_push(){
    echo "Building repository"
    pwd

    docker build -t sidravic/clumsy_phantom:"${BRANCH_NAME}_${COMMIT_ID}" .
    docker tag sidravic/clumsy_phantom:"${BRANCH_NAME}_${COMMIT_ID}" sidravic/clumsy_phantom:latest
    docker tag sidravic/clumsy_phantom:"${BRANCH_NAME}_${COMMIT_ID}" "${GITLAB_REGISTRY}/sidravic/clumsy_phantom:${BRANCH_NAME}_${COMMIT_ID}"
    docker tag sidravic/clumsy_phantom:"${BRANCH_NAME}_${COMMIT_ID}" "${GITLAB_REGISTRY}/sidravic/clumsy_phantom:latest"
    docker push "${GITLAB_REGISTRY}/sidravic/clumsy_phantom:${BRANCH_NAME}_${COMMIT_ID}"
}

function export_image_locally(){
    echo "${GITLAB_REGISTRY}/sidravic/clumsy_phantom:${BRANCH_NAME}_${COMMIT_ID}"
    export LOST_GRANDMA_IMAGE_ID="${GITLAB_REGISTRY}/sidravic/clumsy_phantom:${BRANCH_NAME}_${COMMIT_ID}"
}

function predictor(){
    login_ecs
    get_branch_name
    get_commit_id
    predictor_build_and_push
    export_image_locally
}

function main(){    
    arg1=$1
    arg2=$2

    echo "${arg1} ${arg2}"
    predictor
}


main $1 $2

