# java-imports-files-relations

This plugin builds relationships between the project files based on the imports used by each file, taking into account only the imports that represent files from the analyzed project

# Run the plugin

To run the plugin try: python3 main.py ${OutputFile} ${RootFolder}

The plugin scans all the files in the RootFolder and builds an OutputFile file with all the information necessary to run the plugin on dx-platform.

#Results

The results were obtained by analyzing the "spring-boot" project and are returned by the plugin as a JSON file. These results can be seen in the results.json file.

# Spring-boot repository link: 

	https://github.com/spring-projects/spring-boot

# Docker Hub image link: https://hub.docker.com/repository/docker/bogdanbercea/ces_java_imports_files_relations

