package br.com.resultfacil.resultserver.utils.storage;

import java.io.InputStream;
import java.util.UUID;

import lombok.Builder;
import lombok.Getter;

public interface FileStorageService {

    FileDow dowFile(String fileName);

    void upfile(FileNew fileNew);

    void delFile(String fileName);

    default void repFile(String oldFileName, FileNew fileNew) {
        this.upfile(fileNew);

        if (!oldFileName.equals(null)) {
            this.delFile(oldFileName);
        }
    }

    default String generateFileName(String originName) {
        return UUID.randomUUID().toString() + "_" + originName;
    }

    @Builder
    @Getter
    class FileNew {

        private String fileName;
        private String contentType;
        private InputStream inputStream;

    }

    @Builder
    @Getter
    class FileDow {
        private InputStream inputStream;
    }

}