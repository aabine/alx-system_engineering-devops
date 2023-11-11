file_line { 'replace':
  path    => '/var/www/html/wp-settings.php',
  line    => '/phpp/php/',
  match   => '.*',
  require => Exec['create_file'],
}

exec { 'create_file':
  command => 'touch /var/www/html/wp-settings.php',
  creates => '/var/www/html/wp-settings.php',
}