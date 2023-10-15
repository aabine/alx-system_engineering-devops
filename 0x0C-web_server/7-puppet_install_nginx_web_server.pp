# Update the package manager and install Nginx
exec { 'update_package_manager':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
  require => Package['nginx'],
}

package { 'nginx':
  ensure => installed,
}

# Allow HTTP traffic through the firewall
class { 'ufw':
  before => Service['nginx'],
}

ufw::allow { 'Nginx HTTP':
  before => Service['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

$redirect = "server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/aabine permanent;"

file_line { 'nginx_redirect':
  path  => '/etc/nginx/sites-enabled/default',
  line  => $redirect,
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
}

$new_404_page = "listen 80 default_server;\n\terror_page 404 \/404.html;\n\tlocation = \/404.html {\n\t\troot \/var\/www\/html;\n\t\tinternal;\n\t}"

file_line { 'nginx_404_page':
  path => '/etc/nginx/sites-enabled/default',
  line => $new_404_page,
}

exec { 'test_nginx_config':
  command => '/usr/sbin/nginx -t',
  path    => '/usr/sbin',
  require => [Package['nginx'], File_line['nginx_redirect'], File_line['nginx_404_page']],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  hasstatus => true,
  require   => Exec['test_nginx_config'],
}
