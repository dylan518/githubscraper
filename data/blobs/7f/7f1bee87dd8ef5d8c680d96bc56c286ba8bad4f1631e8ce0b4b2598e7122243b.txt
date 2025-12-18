package Tester;


import Book.BookCopy;
import Book.BookDetails;
import DataAccessor.DBAccessor;
import ID.IdGenerator;
import Library.Library;
import Searcher.*;
import authentication.UserAuthenticator;

import javax.swing.*;
import User.Member;
import java.util.Date;
import java.util.List;

public class Tester {
    private final Library library=new Library(new DBAccessor());
    public List<BookCopy>searchBookByBookName(String bookname){
        if(bookname==null)
        {
           throw new IllegalArgumentException("Book Name can't be null");
        }
        BookSearcher bookSearcher=new NameBaseBookSearcher(bookname);
        return bookSearcher.search();
    }
    public List<BookCopy>searchBookByAuthorName(List<String>authorNames)
    {
        if(authorNames==null||authorNames.size()==0)
        {
            throw new IllegalArgumentException("authorNames can't be null");
        }
        BookSearcher bookSearcher=new AuthorBasedBookSearcher(authorNames);
        return bookSearcher.search();

    }
    public List<Member> searchMemberByMemberName(String memberName,String adminToken) throws IllegalAccessException {
        if(!UserAuthenticator.isAdmin(adminToken))
        {
            throw new IllegalAccessException("Operation forbidden");
        }
        MemberSearcher memberSearcher=new NameBasedMemberSearcher(memberName);
                return memberSearcher.search();

    }
   public void addBook(String bookName, Date publicationDate, List<String>authors, String adminToeken) throws IllegalAccessException {
        if(!UserAuthenticator.isAdmin(adminToeken))
        {
            throw new IllegalAccessException("Operation forbidden");
        }

//        validation based  logic here
      BookCopy bookCopy= new BookCopy(new BookDetails(bookName,publicationDate,authors), IdGenerator.getUniqueId());
        library.addBookCopy(bookCopy);
    }
    public void deleteBook(int bookCopyId,String adminTopken)
    {
        if(bookCopyId<=0 || adminTopken==null || adminTopken.length()==0)
        {
            throw new IllegalArgumentException("bookCopyId/adminToken cannot be NULL or empty");
        }
        BookSearcher bookSearcher=new IdBasedBookSearcher(bookCopyId);
        List<BookCopy>bookCopies=bookSearcher.search();
        if(bookCopies==null || bookCopies.size()==0)
        {
            throw new RuntimeException("No book copies retrieved for given Id");
        }
        library.deleteBookCopy(bookCopies.get(0));


    }
    public void blockMember(int memberId,String adminToken) throws IllegalAccessException {
        if(memberId <0|| adminToken==null ||adminToken.length()==0)
        {

        }
        if(!UserAuthenticator.isAdmin(adminToken))
        {
            throw new IllegalAccessException("Operation forbidden");
        }
        MemberSearcher memberSearcher=new IdBasedMemberSearcher(memberId);
       List<Member> members= memberSearcher.search();
        if(members==null || members.size()==0)
        {
            throw new RuntimeException("No member copies retrieved for given id");
        }
        library.blockMember(members.get(0));
    }
    public void issueBook(int bookCopyId,int memberID,String adminToken)
    {
        BookSearcher bookSearcher=new IdBasedBookSearcher(bookCopyId);
        List<BookCopy>bookCopies=bookSearcher.search();
        if(bookCopies==null || bookCopies.size()==0)
        {
            throw new RuntimeException("No book copies retrieved for given Id");
        }

        MemberSearcher memberSearcher=new IdBasedMemberSearcher(memberID);
        List<Member> members=memberSearcher.search();
        if(members==null ||members.size()==0)
        {
            throw new RuntimeException("No members retrieved for given id");
        }
       library.issueBook(bookCopies.get(0),members.get(0));
    }
    public void submitBook(int bookCopyId,int memberId,String adminToken)
    {

    }
    public Member getBorrowerOfBook(int bookCopyId,String adminToken)
    {
        return null;

    }
    public List<BookCopy> getBooksBorrowedByMember(int memberId,String adminToken){
        return null;
    }
}
