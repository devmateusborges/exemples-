// ==============================
export const UtilValidEmail = (email: string) => {
  return /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(email);
};
// ==============================
export const formatDateColumn = (value: any, format: any = null) => {
  // console.log("formatDateColumn",value);
  return value.toLocaleDateString(
    "en-US",
    format ?? {
      day: "2-digit",
      month: "2-digit",
      year: "numeric",
    }
  );
};
// ==============================
export const formatDateTimeColumn = (value: any, lng = "en-US") => {
  // console.log("formatDateColumn",value);

  return value.toLocaleDateString(lng, {
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
    hourCycle: "h24",
  });
};
// ==============================
export const formatCurrencyColumn = (value: any, lng = "en-US", minDig = 2) => {
  const val = Intl.NumberFormat(lng, {
    minimumFractionDigits: minDig,
  }).format(value);
  // console.log(val);
  return val;
};
// ==============================
export const randomArray = (limit: number) => {
  const content = [];
  for (let i = 0; i < limit; i += 1) {
    content.push(i);
  }
  return content;
};

export const capitalize = (
  [first, ...rest]: [first: any, ...rest: any],
  locale = navigator.language
) => {
  return first === undefined
    ? ""
    : first.toLocaleUpperCase(locale) + rest.join("");
};

export const openDownloadFolder = (url: string) => {
  const link = document.createElement("a");
  link.setAttribute("download", "teste");
  link.href = url;
  document.body.appendChild(link);
  link.click();
  link.remove();
};
