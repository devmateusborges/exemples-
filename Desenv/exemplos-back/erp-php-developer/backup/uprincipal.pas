unit uPrincipal;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, ExtCtrls, Buttons,
  ActnList, StdCtrls, ComCtrls;

type

  { TFrmPrincipal }

  TFrmPrincipal = class(TForm)
    AclPrincipal: TActionList;
    AclSair: TAction;
    AclTabelas: TAction;
    AclConfigs: TAction;
    BtnTabelas: TSpeedButton;
    BtnConfigs: TSpeedButton;
    ImgLogo: TImage;
    ImgPrincipal: TImageList;
    Label1: TLabel;
    PgPrincipal: TPageControl;
    PnlMenuLeft: TPanel;
    PnlMenuTop: TPanel;
    BtnSair: TSpeedButton;
    StbPrincipal: TStatusBar;
    procedure AclConfigsExecute(Sender: TObject);
    procedure AclSairExecute(Sender: TObject);
    procedure AclTabelasExecute(Sender: TObject);
    procedure ImgLogoClick(Sender: TObject);
    procedure PgPrincipalChange(Sender: TObject);
    procedure PgPrincipalMouseDown(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
  private

  public
    procedure ProcAbaNova(ClasseForm: string); overload;
    function FuncAbaPodeAbrirFormulario(ClasseForm: TFormClass; var TabSheet: TTabSheet): Boolean;
    procedure ProcAbaAjustarCaption(ClasseForm: TFormClass);
    function FuncAbaTotalFormsAbertos(ClasseForm: TFormClass) : Integer;
  end;

var
  FrmPrincipal: TFrmPrincipal;

implementation

{$R *.lfm}

{ TFrmPrincipal }

procedure TFrmPrincipal.AclSairExecute(Sender: TObject);
begin
  Application.Terminate;
end;

procedure TFrmPrincipal.AclTabelasExecute(Sender: TObject);
begin
  //
end;

procedure TFrmPrincipal.ImgLogoClick(Sender: TObject);
begin

end;

procedure TFrmPrincipal.PgPrincipalChange(Sender: TObject);
begin
  Caption := PgPrincipal.ActivePage.Caption;
  Application.Title := Caption;

  with (PgPrincipal.ActivePage.Components[0] as TForm) do
    if not Assigned(Parent) then
      Show;
end;

procedure TFrmPrincipal.PgPrincipalMouseDown(Sender: TObject;
  Button: TMouseButton; Shift: TShiftState; X, Y: Integer);
begin
    if Button = mbRight then
    PgPrincipal.ActivePageIndex := PgPrincipal.IndexOfTabAt(X, Y);
end;

procedure TFrmPrincipal.AclConfigsExecute(Sender: TObject);
begin
  ProcAbaNova('TFrmConfig');
end;


procedure TFrmPrincipal.ProcAbaNova(ClasseForm: string);
var
  vClasseForm: TFormClass;
  TabSheet: TTabSheet;
  Form: TForm;
begin

    try
      PgPrincipal.Options:=[nboShowCloseButtons];

      vClasseForm := TFormClass(FindClass(trim(ClasseForm)));
      if not FuncAbaPodeAbrirFormulario(vClasseForm, TabSheet) then
      begin
        PgPrincipal.ActivePage := TabSheet;
        exit;
      end;

      TabSheet := TTabSheet.Create(Self);
      TabSheet.PageControl := PgPrincipal;

      Form := vClasseForm.Create(TabSheet);

      with Form do
      begin
        if FindComponent('AclSair') <> nil then
        begin
          TAction(FindComponent('AclSair')).Visible := false;
        end;

        Align := alClient;
        BorderStyle := bsNone;
        Visible := true;
//TODO        Caption := qryTelasTITULO.AsString;
        KeyPreview := True;
        Parent := TabSheet; // Ja da Show
      end;

      with TabSheet do
      begin
        Caption := UpperCase(Form.Caption);
      end;

      ProcAbaAjustarCaption(vClasseForm);


      PgPrincipal.ActivePage := TabSheet;

      PgPrincipalChange(PgPrincipal);

    except
      on E: Exception do
      begin
        MessageDlg('Erro ao abrir fomulario [' + E.Message + ']', mtError ,[mbClose],0);
      end;
    end;

end;


function TFrmPrincipal.FuncAbaPodeAbrirFormulario(ClasseForm: TFormClass; var TabSheet: TTabSheet): Boolean;
var
  I: Integer;
begin
  Result := true;

  for I := 0 to PgPrincipal.PageCount - 1 do
    if PgPrincipal.Pages[I].Components[0].ClassType = ClasseForm then
    begin
      TabSheet := PgPrincipal.Pages[I];
      Result := false;
      Break;
    end;

end;

procedure TFrmPrincipal.ProcAbaAjustarCaption(ClasseForm: TFormClass);
var
  I, Indice, TotalForms: Integer;
begin
  TotalForms := FuncAbaTotalFormsAbertos(ClasseForm);

  if TotalForms > 1 then
  begin
    Indice := 1;
    for I := 0 to PgPrincipal.PageCount - 1 do
      with PgPrincipal do
        if Pages[I].Components[0].ClassType = ClasseForm then
        begin
          Pages[I].Caption := (Pages[I].Components[0] as TForm).Caption + ' (' +
            IntToStr(Indice) + ')';
          Inc(Indice);
        end;
  end;
end;

function TFrmPrincipal.FuncAbaTotalFormsAbertos(ClasseForm: TFormClass) : Integer;
var
  I: Integer;
begin
  Result := 0;
  for I := 0 to PgPrincipal.PageCount - 1 do
    if PgPrincipal.Pages[I].Components[0].ClassType = ClasseForm then
      Inc(Result);
end;

end.

