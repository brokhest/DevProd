cd ..

pip freeze > requirements.txt
git add .
git commit -m "deployed_dev"
git push 

ssh -i E:/dossh/key root@167.99.245.100 'cd .. && cd home/broha/site/Development/DevProd/scripts && sh build.sh'
