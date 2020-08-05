kolla-ansible -i ./all-in-one bootstrap-servers
kolla-ansible -i ./all-in-one deploy
kolla-ansible -i ./all-in-one post-deploy
cp /etc/kolla/admin-openrc.sh ~/backup/
. /etc/kolla/admin-openrc.sh
./init-runonce
openstack server create \
    --image cirros \
    --flavor m1.tiny \
    --key-name mykey \
    --network demo-net \
    demo1
