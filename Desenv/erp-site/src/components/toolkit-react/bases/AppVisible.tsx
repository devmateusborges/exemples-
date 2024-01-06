import IAppProps from "../interface/IAppProp";

interface IAppVisible extends IAppProps {
  visible: boolean | undefined | string | null;
}

const AppVisible: React.FC<IAppVisible> = ({
  children,
  visible,
}: IAppVisible) => {
  return (
    <>
      {(() => {
        if (visible === "" || !visible) {
          return <></>;
        }
        return <> {children} </>;
      })()}
    </>
  );
};

export default AppVisible;
