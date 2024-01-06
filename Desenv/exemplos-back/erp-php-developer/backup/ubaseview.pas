unit ubaseview;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, ActnList, ExtCtrls,
  Buttons, StdCtrls;

type

  { TFrmBaseView }

  TFrmBaseView = class(TForm)
    AclBase: TActionList;
    AclSair: TAction;
    BtnSair: TSpeedButton;
    PnlMenuTop: TPanel;
    procedure AclSairExecute(Sender: TObject);
  private

  public
    function IsFormParented(aForm:TForm):Boolean;inline;
  end;

var
  FrmBaseView: TFrmBaseView;

implementation

{$R *.lfm}

{ TFrmBaseView }

procedure TFrmBaseView.AclSairExecute(Sender: TObject);
begin
 if isformParented(Self) then parent.free
  else close;
end;

function TFrmBaseView.IsFormParented(aForm:TForm):Boolean;inline;
begin
  result := aForm.Parent<>nil
end;

end.

