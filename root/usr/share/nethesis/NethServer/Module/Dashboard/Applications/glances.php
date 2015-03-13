<?php
namespace NethServer\Module\Dashboard\Applications;

/**
 * glances web interface
 *
 * @author stephane de labrusse
 */
class glances extends \Nethgui\Module\AbstractModule implements \NethServer\Module\Dashboard\Interfaces\ApplicationInterface
{

    public function getName()
    {
        return "Glances";
    }

    public function getInfo()
    {
         $port = $this->getPlatform()->getDatabase('configuration')->getProp('glances','TCPPort');
         $host = explode(':',$_SERVER['HTTP_HOST']);
         return array(
            'url' => "http://".$host[0].":$port"
         );
    }
}


