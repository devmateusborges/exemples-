export default interface IAppProps {
  id?: string;
  appHelpText?: string;
  appRequired?: boolean;
  style?: object;
  className?: string;
  children?: React.ReactNode;
  classNameBorder?: string;
  classNameText?: string;
  classNameBg?: string;
}
