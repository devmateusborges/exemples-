unit uconfigview;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, ActnList, StdCtrls,
  ubaseview;

type

  { TFrmConfig }

  TFrmConfig = class(TFrmBaseView)

  private

  public

  end;

var
  FrmConfig: TFrmConfig;

implementation

{$R *.lfm}

initialization
  Registerclass(TFrmConfig);
end.

