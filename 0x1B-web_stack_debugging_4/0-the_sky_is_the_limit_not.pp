# 0-the_sky_is_the_limit_not.pp
# This Puppet manifest configures Nginx to handle more concurrent connections to fix the high number of failed requests.

exec { 'increase_worker_connections':
  command => 'sed -i "s/worker_connections [0-9]\+/worker_connections 1024/" /etc/nginx/nginx.conf',
  onlyif  => 'grep -q "worker_connections [0-9]\+" /etc/nginx/nginx.conf',
}

exec { 'increase_worker_processes':
  command => 'sed -i "s/worker_processes [0-9]\+/worker_processes auto/" /etc/nginx/nginx.conf',
  onlyif  => 'grep -q "worker_processes [0-9]\+" /etc/nginx/nginx.conf',
}

service { 'nginx':
  ensure => 'running',
  enable => true,
  subscribe => Exec['increase_worker_connections'],
}

exec { 'reload_nginx':
  command     => 'nginx -s reload',
  refreshonly => true,
  subscribe   => [ Exec['increase_worker_connections'], Exec['increase_worker_processes'] ],
}
