CONTAINER_ID=$(sudo docker ps | grep bitnami | sed 's/|/ /' | awk '{print $1}')
CONTAINER_OUTPUT=reddit/data/output
OUTPUT=reddit/app/data/output


echo "Running benchmark using spark master with container ID $CONTAINER_ID"
echo "===== $(date)" >> $OUTPUT

for INPUT_FILE in RC_2009-05
do
    for CORE_COUNT in 1 2 4 8 16 32
    do
        sudo docker exec -it $CONTAINER_ID spark-submit reddit/project.py -i reddit/data/$INPUT_FILE -c $CORE_COUNT -s -r -o $CONTAINER_OUTPUT
    done
done