<?php

class SystemProgramComponentService
{

    public static function MontaJSTour($pController)
    {

        TTransaction::open(TSession::getValue('pConn'));
        $pcs = SystemProgramComponent::where('system_program_id', 'IN', '(select id from system_program where controller=' . "'" . $pController . "'" . ')')
            ->orderBy('order_view')->load();
        $vSc = "function " . $pController . "Tour () {var tour = new Tour({ name: 'Tour_$pController', prev: 0, next: 1, steps: [";
        foreach ($pcs as $pc) {
            $vSc = $vSc . " {element: \".".$pc->component_element."\", title: \"".$pc->title."\", content: \"" . $pc->content ." <br><br> <a href='". $pc->link_video ."' target='_blank'>Assistir Video</a><br><a href='". $pc->link_manual ."/".  $pController ."' target='_blank'>Acessar Manual</a>\"},";
        }
        $vSc = $vSc . "]});  tour.start(true);";

        foreach ($pcs as $pc) {
            $vSc = $vSc . "$('.".$pc->component_element."').attr(\"data-toggle\", \"tooltip\");";
            $vSc = $vSc . "$('.".$pc->component_element."').attr(\"data-placement\", \"bottom\");";
            $vSc = $vSc . "$('.".$pc->component_element."').attr(\"data-html\", \"true\");";
            $vSc = $vSc . "$('.".$pc->component_element."').attr(\"data-boundary\", \"scrollParent\");";
            $vSc = $vSc . "$('.".$pc->component_element."').attr(\"title\", \"".$pc->title."\");";
        }

        $vSc = $vSc . "};";
        TTransaction::close();
        return $vSc;
    }

    public static function MontaJSTooltip($pController)
    {

        $vSc = "function " . $pController . "Tooltip () {";
        $vSc = $vSc . "$('[data-toggle=\"tooltip\"]').tooltip(); }";
        return $vSc;
    }


    public static function MontaExecJSCarreg($pController)
    {
        $vSc = " $(document).ready(function() { " . $pController . "Tooltip() });";
        return $vSc;
    }
}
