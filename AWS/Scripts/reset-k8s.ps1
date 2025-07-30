# נתיב לקובץ kustomization.yaml
$k8sPath = "C:\Users\user\Desktop\DATA\Projects\NaiveBayesProject\AWS"

Write-Host "🔻 מוחק את כל המשאבים הקיימים..." -ForegroundColor Red

# מחיקת כל המשאבים הרלוונטיים
kubectl delete all --all
kubectl delete pvc --all
kubectl delete pv --all
kubectl delete storageclass efs-sc

Start-Sleep -Seconds 20

Write-Host "🚀 מקים הכל מחדש עם kubectl apply -k $k8sPath" -ForegroundColor Cyan
kubectl apply -k $k8sPath

Write-Host "✅ כל המשאבים עלו מחדש בהצלחה!" -ForegroundColor Green
