cd ../

pip freeze > requirements.txt
git add .
git commit -m "deployed_dev"
git push 

ssh -i E:\do ssh\key broha@167.99.245.100 'cd ~/site/Development/DevProd/scripts && ./build.sh'
