export const formatDateTimeColumn = (value: any, lng = "en-US") => {
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
