@REM  הצגת פרוייקטים קיימים
oc get project   
@REM מחיקת פרוייקט
oc delete <name>
@REM יצירת פרוייקט 
oc new-project <data-loader>




oc project tejendrarana-dev
oc new-app --as-deployment-config --docker-image=registry.access.redhat.com/rhscl/mysql-57-rhel7:latest --name=mysql-openshift -e MYSQL_USER=user1 -e MYSQL_PASSWORD=mypa55 -e MYSQL_DATABASE=testdb -e MYSQL_ROOT_PASSWORD=r00tpa55
oc status
oc get pods
oc describe pod {pod-id}
oc get svc
oc describe service mysql-openshift
oc describe dc mysql-openshift
oc expose service mysql-openshift
oc get routes
oc port-forward {pod-id} 3306:3306