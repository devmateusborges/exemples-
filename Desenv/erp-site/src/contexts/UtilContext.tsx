"use client";
import { createContext, useContext, useState } from "react";

interface UtilProviderProps {
  children?: React.ReactNode;
}

export type UtilContextType = {
  loading: Boolean;
  setLoading: (value: boolean) => void;
};

const UtilContext = createContext<UtilContextType | null>(null);

export const UtilProvider: React.FC<UtilProviderProps> = ({ children }) => {
  const [loading, setLoading] = useState(false);
  return (
    <UtilContext.Provider value={{ loading, setLoading }}>
      {children}
    </UtilContext.Provider>
  );
};

export function useUtilContext() {
  const context = useContext(UtilContext);
  if (!context) {
    throw new Error("useLoading must be used within LoadingProvider");
  }
  return context;
}
