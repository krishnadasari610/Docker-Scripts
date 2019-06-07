FROM rapiscansystems/malibu-mainapp-base:configured

#copy all files to destination directory 
COPY . $MALIBU_SETUP_SCRIPTS_DIRECTORY
#Assigning Owner permissions to destination directory
RUN chown -hR $ZICONS_USERNAME:$ZICONS_USERNAME $MALIBU_SETUP_SCRIPTS_DIRECTORY
#USER NAME
USER $ZICONS_USERNAME
#Folder permissions provided 
RUN chmod +x -R $MALIBU_SETUP_SCRIPTS_DIRECTORY
# executes script file and create rapiscan and its subfolder 
RUN $MALIBU_SETUP_SCRIPT

# login with specified directory
WORKDIR $WORK_DIRECTORY

ENTRYPOINT ["./MainApp","DCSD","--verbose","--console"]
