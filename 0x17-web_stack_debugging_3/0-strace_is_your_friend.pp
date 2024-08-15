# Fixes a wordpress site tha is running in the apache2 server.
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php; sudo service apache2 restart',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
