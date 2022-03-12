g13_k1	130.238.28.53
g13_k2	130.238.28.52

Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 192.168.2.230:6443 --token 1lhhnk.t9et9tab60v5a4ai --discovery-token-ca-cert-hash sha256:aa4928c667a9a9e0f8588ecebb12db55eb6bc62bad5e8e18826aeec004a9fe35


localhost issue fix init
https://www.mirantis.com/blog/how-install-kubernetes-kubeadm/

localhost issue fix join
https://stackoverflow.com/a/69794366/1370869
